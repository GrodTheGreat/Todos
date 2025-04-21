package controllers

import (
	"html/template"
	"net/http"
	"path/filepath"
	"todo/database"
	"todo/models"

	"github.com/gin-gonic/gin"
)

func CreateTodo(c *gin.Context) {}

func DeleteTodo(c *gin.Context) {
	// id := c.Param("id")
}

func GetTodo(c *gin.Context) {
	// id := c.Param("id")

}

func GetTodos(c *gin.Context) {
	var todos []models.Todo

	result := database.GetDB().Find(&todos)
	if result.Error != nil {
		return
	}

	tmpl, err := template.ParseFiles(filepath.Join("templates", "todos", "index.html"))
	if err != nil {
		c.String(http.StatusInternalServerError, "Template error")
		return
	}

	c.Header("Content-Type", "text/html")
	tmpl.Execute(c.Writer, todos)
}

func UpdateTodo(c *gin.Context) {
	// id := c.Param("id")
}
