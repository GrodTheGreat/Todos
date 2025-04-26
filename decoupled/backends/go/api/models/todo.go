package models

import (
	"time"

	"gorm.io/gorm"
)

type Todo struct {
	gorm.Model
	UserID      uint
	Title       string
	Description *string
	Due         *time.Time
	IsCompleted bool
	PriorityID  *uint
	StatusID    *uint
	Tags        []Tag
	Reminder    *Reminder
}

type Tag struct {
	gorm.Model
	UserID uint
	TodoID uint
	Name   string
}

type Reminder struct {
	gorm.Model
	TodoID   uint
	RemindAt time.Time
}

type Priority struct {
	gorm.Model
	Name  string
	Level uint
	Todos []Todo
}

type Status struct {
	gorm.Model
	Name  string
	Level uint
	Todos []Todo
}
