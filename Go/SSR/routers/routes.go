package routes

import (
	"todo/controllers"

	"github.com/gin-gonic/gin"
)

func SetupRoutes(r *gin.Engine) {
	r.GET("/login", controllers.RenderLogin)
	r.POST("/login", controllers.Login)
	r.GET("/register", controllers.RenderRegister)
	r.POST("/register", controllers.Register)

	todos := r.Group("/todos")
	{
		todos.POST("", controllers.CreateTodo)
		todos.GET("", controllers.GetTodos)
		todos.GET("/:id", controllers.GetTodo)
		todos.DELETE("/:id", controllers.DeleteTodo)
		todos.PUT("/:id", controllers.UpdateTodo)
	}
}
