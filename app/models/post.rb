class Post < ActiveRecord::Base
  attr_accessible :about_text, :author_id, :category_id, :link_url, :post_at, :status, :thumb_url, :title
  belongs_to :category
  belongs_to :author
end
