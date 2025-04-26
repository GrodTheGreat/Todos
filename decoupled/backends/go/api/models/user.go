package models

import (
	"time"

	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Username     string
	GivenName    *string
	Surname      *string
	Email        string
	PasswordHash string
	IsActive     bool
	LastLogin    *time.Time
	Todos        []Todo
	Tags         []Tag
	Settings     Settings
	ActivityLogs []ActivityLog
}
