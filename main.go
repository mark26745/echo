package main

import (
	"fmt"
	"log"
	"os"

	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New(fiber.Config{
		Prefork: false,
	})

	//Healthcheck
	app.Get("/health", func(c *fiber.Ctx) error {
		return c.SendStatus(200)
	})

	//Routes
	app.Post("/dump", func(c *fiber.Ctx) error {
		dump := string(c.Body())
		log.Print(dump)
		return c.SendString(dump)
	})

	// Start app
	log.Fatal(app.Listen(fmt.Sprintf("0.0.0.0:%s", os.Getenv("PORT"))))
}
