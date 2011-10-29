require 'spec_helper'

module CookbookBump

  describe Bump do
    before :all do
      @bumper = Bump.new
      @cookbook_path = File.dirname(__FILE__)
    end

    describe "patch" do
      it "should increment the cookbook patch level in the metadata by one" do
        original_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        original_patch_level = original_version.split('.').last.to_i
        @bumper.patch(@cookbook_path, "example_cookbook")
        bumped_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        bumped_patch_level = bumped_version.split('.').last.to_i
        result = bumped_patch_level - original_patch_level
        result.should eq(1)
      end
    end

    describe "minor" do
      it "should increment the cookbook minor level in the metadata by one" do
        original_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        original_patch_level = original_version.split('.')[1].to_i
        @bumper.minor(@cookbook_path, "example_cookbook")
        bumped_version = @bumper.get_version(@cookbook_path, "example_cookbook")
        bumped_patch_level = bumped_version.split('.')[1].to_i
        result = bumped_patch_level - original_patch_level
        result.should eq(1)
      end
    end

  end
end
