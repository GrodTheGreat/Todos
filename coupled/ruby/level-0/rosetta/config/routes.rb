Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
  get "/todos", to: "todos#index"

  get "/todos/create", to: "todos#create"
  post "/todos/create", to: "todos#create"

  get "/todos/:id", to: "todos#get_by_id"

  get "/todos/:id/edit", to: "todos#update"
  post "/todos/:id/edit", to: "todos#update"

  get "/todos/:id/delete", to: "todos#delete"
  post "/todos/:id/delete", to: "todos#delete"

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Render dynamic PWA files from app/views/pwa/* (remember to link manifest in application.html.erb)
  # get "manifest" => "rails/pwa#manifest", as: :pwa_manifest
  # get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker

  # Defines the root path route ("/")
  # root "posts#index"
end
