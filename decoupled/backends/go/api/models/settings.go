package models

import (
	"gorm.io/gorm"
)

type Settings struct {
	gorm.Model
	UserID                   uint
	ThemeID                  uint
	NotificationPreferenceID uint
}

type Theme struct {
	gorm.Model
	Preference string
	Settings   []Settings
}

type NotificationPreference struct {
	gorm.Model
	Preference string
	Settings   []Settings
}
