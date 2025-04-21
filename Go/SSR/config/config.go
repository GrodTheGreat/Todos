package config

import (
	"os"

	"github.com/joho/godotenv"
)

type Config struct {
	Port      string
	DBConnStr string
}

func LoadConfig() (*Config, error) {
	if err := godotenv.Load(); err != nil {
		return nil, err
	}

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	dbStr := os.Getenv("DATABASE_URL")
	if dbStr == "" {
		dbStr = "./database/default.db"
	}

	return &Config{
		Port:      port,
		DBConnStr: dbStr,
	}, nil
}
