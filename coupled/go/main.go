package main

import (
	"log"
	"todo/config"
	"todo/database"
	"todo/models"
	routes "todo/routers"

	"github.com/gin-gonic/gin"
)

func main() {
	config, err := config.LoadConfig()
	if err != nil {
		log.Printf("Error loading config: %v", err)
	}

	err = database.InitDB(config.DBConnStr)
	if err != nil {
		log.Fatal("Failed to connect to database:", err)
	}

	db := database.GetDB()
	err = db.AutoMigrate(&models.User{}, &models.Todo{})
	if err != nil {
		log.Fatal("Failed to migrate database:", err)
	}

	router := gin.Default()
	routes.SetupRoutes(router)

	log.Printf("Server starting on port %s", config.Port)
	err = router.Run(":" + config.Port)
	if err != nil {
		log.Fatal("Failed to start server:", err)
	}
}
