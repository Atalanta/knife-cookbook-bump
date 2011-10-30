require 'spec_helper'

module CookbookBump

  describe Bump do
    before :all do
      @bumper = Bump.new
      @cookbook_path = File.dirname(__FILE__)
      @index = { "major" => 0, "minor" => 1, "patch" => 2 }
    end

    describe "patch" do
      it "should increment the cookbook patch level in the metadata by one" do
        original_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        original_patch_level = original_version.split('.')[@index["patch"]].to_i
        @bumper.patch(@cookbook_path, "example_cookbook", "patch")
        bumped_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        bumped_patch_level = bumped_version.split('.')[@index["patch"]].to_i
        result = bumped_patch_level - original_patch_level
        result.should eq(1)
      end
    end

    describe "minor" do
      it "should increment the cookbook minor level in the metadata by one" do
        original_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        original_patch_level = original_version.split('.')[@index["minor"]].to_i
        @bumper.patch(@cookbook_path, "example_cookbook", "minor")
        bumped_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        bumped_patch_level = bumped_version.split('.')[@index["minor"]].to_i
        result = bumped_patch_level - original_patch_level
        result.should eq(1)
      end
    end

    describe "major" do
      it "should increment the cookbook minor level in the metadata by one" do
        original_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        original_patch_level = original_version.split('.')[@index["major"]].to_i
        @bumper.patch(@cookbook_path, "example_cookbook", "major")
        bumped_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        bumped_patch_level = bumped_version.split('.')[@index["major"]].to_i
        result = bumped_patch_level - original_patch_level
        result.should eq(1)
      end
    end

    describe "tag" do
      it "should tag the git repository in which the cookbook resides with the bumped version number" do
        puts "Cookbook path: #{@cookbook_path}"
        existing_tags = @bumper.get_tags(@cookbook_path, "example_cookbook")
        puts "Tags: #{existing_tags}"
        @bumper.patch(@cookbook_path, "example_cookbook", "patch")
        latest_version =  @bumper.get_version(@cookbook_path, "example_cookbook")
        @bumper.tag
        latest_tags = @bumper.get_tags(@cookbook_path, "example_cookbook")
        new_tag = latest_tags - existing_tags
        new_tag.should eq(latest_version)
      end
    end

  end
end
