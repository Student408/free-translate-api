package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net/http"
	"html/template"

	"github.com/bregydoc/gtranslate"
	"github.com/rs/cors"
)

var enableLogs = flag.Bool("logs", false, "Enable detailed logging")

type TranslateRequest struct {
	Text string `json:"text"`
	To   string `json:"to"`
}

type TranslateResponse struct {
	TranslatedText string `json:"translatedText,omitempty"`
	Status         bool   `json:"status"`
	Message        string `json:"message"`
}

func TranslateHandler(w http.ResponseWriter, r *http.Request) {
	if *enableLogs {
		log.Println("Received translation request")
	}

	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var request TranslateRequest
	err := json.NewDecoder(r.Body).Decode(&request)
	if err != nil {
		sendErrorResponse(w, "Invalid request payload", http.StatusBadRequest)
		return
	}

	translated, err := gtranslate.TranslateWithParams(request.Text, gtranslate.TranslationParams{
		From: "auto",
		To:   request.To,
	})
	if err != nil {
		sendErrorResponse(w, "Translation failed", http.StatusInternalServerError)
		return
	}

	response := TranslateResponse{
		TranslatedText: translated,
		Status:         true,
		Message:        "",
	}

	sendJSONResponse(w, response, http.StatusOK)
}

func sendErrorResponse(w http.ResponseWriter, message string, statusCode int) {
	response := TranslateResponse{
		Status:  false,
		Message: message,
	}
	sendJSONResponse(w, response, statusCode)
}

func sendJSONResponse(w http.ResponseWriter, data interface{}, statusCode int) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(statusCode)
	err := json.NewEncoder(w).Encode(data)
	if err != nil {
		log.Printf("Failed to encode JSON response: %v", err)
	}
}

func HealthHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"status":"healthy"}`))
}

func GuideHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("guide.html"))
	tmpl.Execute(w, nil)
}

func main() {
	flag.Parse()

	mux := http.NewServeMux()
	mux.HandleFunc("/translate", TranslateHandler)
	mux.HandleFunc("/health", HealthHandler)
	mux.HandleFunc("/", GuideHandler)
	// mux.HandleFunc("/guide", GuideHandler)

	c := cors.Default().Handler(mux)

	fmt.Println("Starting server on http://localhost:8000")
	log.Fatal(http.ListenAndServe(":8000", c))
}
