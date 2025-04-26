package models

import (
	"time"

	"gorm.io/gorm"
)

type ActivityLog struct {
	gorm.Model
	UserID    uint
	ActionID  uint
	Timestamp time.Time
}

type Action struct {
	gorm.Model
	Name         string
	ActivityLogs []ActivityLog
}
