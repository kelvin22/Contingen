class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.string :title
      t.text :about_text
      t.text :link_url
      t.text :thumb_url
      t.integer :category_id
      t.integer :author_id
      t.string :status
      t.datetime :post_at

      t.timestamps
    end
  end
end
