class PostsController < ApplicationController
  def home
    @categories = Category.where( enabled: true )
  end
end
