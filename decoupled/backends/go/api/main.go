package main

import (
	"api/models"
	"fmt"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func main() {
	db, err := gorm.Open(sqlite.Open("todo.db"), &gorm.Config{})
	if err != nil {
		panic("Failed to open database")
	}

	err = db.AutoMigrate(
		models.Action{},
		models.ActivityLog{},
		models.NotificationPreference{},
		models.Priority{},
		models.Reminder{},
		models.Settings{},
		models.Status{},
		models.Tag{},
		models.Theme{},
		models.Todo{},
		models.User{},
	)
	if err != nil {
		panic("Failed to migrate the models")
	}

	fmt.Println("Database created")
}
