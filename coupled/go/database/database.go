package database

import (
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var DB *gorm.DB

func InitDB(connection_string string) error {
	var err error
	DB, err = gorm.Open(sqlite.Open(connection_string), &gorm.Config{})
	if err != nil {
		return err
	}
	return nil
}

func GetDB() *gorm.DB {
	if DB == nil {
		log.Fatal("Database connection not initialized")
	}
	return DB
}
