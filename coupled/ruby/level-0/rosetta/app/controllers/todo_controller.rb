class TodoController < ApplicationController
  def index
    @todos = Todo.all
  end

  def create

  end

  def get_by_id
    @todo = Todo.find(id)
  end

  def update
    @todo = Todo.find(id)
  end

  def delete
    @todo = Todo.find(id)
  end
end
