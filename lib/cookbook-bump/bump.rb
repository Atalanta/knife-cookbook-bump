require 'chef/knife'
require 'chef/cookbook_loader'
require 'chef/cookbook_uploader'

module CookbookBump
  class Bump < Chef::Knife

    def patch(cookbook_path, cookbook)
      current_version = get_version(cookbook_path, cookbook).split(".").map{|i| i.to_i}
      bumped_version = current_version.clone
      bumped_version[2] = bumped_version[2] + 1
      metadata_file = File.join(cookbook_path, cookbook, "metadata.rb")
      update_metadata(current_version.join('.'), bumped_version.join('.'), metadata_file)
    end

    def minor(cookbook_path, cookbook)
      current_version = get_version(cookbook_path, cookbook).split(".").map{|i| i.to_i}
      bumped_version = current_version.clone
      bumped_version[1] = bumped_version[1] + 1
      metadata_file = File.join(cookbook_path, cookbook, "metadata.rb")
      update_metadata(current_version.join('.'), bumped_version.join('.'), metadata_file)
    end

    def update_metadata(old_version, new_version, metadata_file)
      open_file = File.open(metadata_file, "r")
      body_of_file = open_file.read
      open_file.close
      body_of_file.gsub!(old_version, new_version)
      File.open(metadata_file, "w") { |file| file << body_of_file }
    end
    
    def get_version(cookbook_path, cookbook)
      loader = ::Chef::CookbookLoader.new(cookbook_path)
      return loader[cookbook].version
    end
    
  end
end
