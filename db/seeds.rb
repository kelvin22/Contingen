# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

require 'csv'
require 'active_record/fixtures'

ActiveRecord::Fixtures.create_fixtures("#{Rails.root}/db/fixtures", "categories")

CSV.foreach("#{Rails.root}/db/posts.csv", :headers => :first_row) do |row|
  Post.create(:title => row[1],
              :about_text => row[2],
              :link_url => row[3],
              :thumb_url => row[4],
              :category_id => row[5],
              :author_id => row[6],
              :status => row[7],
              :post_at => row[8])
end
