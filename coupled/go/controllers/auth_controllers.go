package controllers

import (
	"html/template"
	"net/http"
	"path/filepath"
	"todo/database"
	"todo/models"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
)

type LoginRequest struct {
	Username string `form:"username"`
	Password string `form:"password"`
}

type RegisterRequest struct {
	Username  string `form:"username"`
	Email     string `form:"email"`
	GivenName string `form:"given-name"`
	Surname   string `form:"surname"`
	Password  string `form:"password"`
	Confirm   string `form:"confirm"`
}

func RenderLogin(c *gin.Context) {
	tmpl, err := template.ParseFiles(filepath.Join("templates", "login.html"))
	if err != nil {
		c.String(http.StatusInternalServerError, "Template error")
		return
	}

	c.Header("Content-Type", "text/html")
	tmpl.Execute(c.Writer, nil)
}

func Login(c *gin.Context) {
	var request LoginRequest

	if err := c.ShouldBind(&request); err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}

	var user models.User
	result := database.DB.Where("username = ?", request.Username).First(&user)
	if result.Error != nil {
		c.String(http.StatusUnauthorized, "Invalid credentials")
		return
	}

	if err := bcrypt.CompareHashAndPassword([]byte(user.PasswordHash), []byte(request.Password)); err != nil {
		c.String(http.StatusUnauthorized, "Invalid credentials")
		return
	}

	// TODO generate session or jwt here
	c.Redirect(http.StatusSeeOther, "/todos")
}

func Logout(c *gin.Context) {

}

func RenderRegister(c *gin.Context) {
	tmpl, err := template.ParseFiles(filepath.Join("templates", "register.html"))
	if err != nil {
		c.String(http.StatusInternalServerError, "Template error")
	}

	c.Header("Content-Type", "text/html")
	tmpl.Execute(c.Writer, nil)
}

func Register(c *gin.Context) {
	// TODO We need a lot more checks on user params
	var request RegisterRequest

	if err := c.ShouldBind(&request); err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}

	if request.Password != request.Confirm {
		c.String(http.StatusBadRequest, "Passwords do not match")
		return
	}

	var existingUser models.User
	if err := database.GetDB().Where("username = ? OR email = ?", request.Username, request.Email).First(&existingUser).Error; err == nil {
		c.String(http.StatusBadRequest, "Username or Email already in use")
		return
	}

	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(request.Password), bcrypt.DefaultCost)
	if err != nil {
		c.String(http.StatusInternalServerError, "Failed to hash password")
		return
	}

	user := models.User{
		Username:     request.Username,
		Email:        request.Email,
		PasswordHash: string(hashedPassword),
		GivenName:    request.GivenName,
		Surname:      request.Surname,
	}

	if err := database.DB.Create(&user).Error; err != nil {
		c.String(http.StatusInternalServerError, "Failed to create user")
		return
	}

	c.Redirect(http.StatusSeeOther, "/login")
}
