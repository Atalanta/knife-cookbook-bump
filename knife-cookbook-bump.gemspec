# -*- encoding: utf-8 -*-
$:.push File.expand_path("../lib", __FILE__)
require "cookbook-bump/version"

Gem::Specification.new do |s|
  s.name        = "knife-cookbook-bump"
  s.version     = Knife::Cookbook::Bump::VERSION
  s.authors     = ["Stephen Nelson-Smith", "Fletcher Nichol"]
  s.email       = ["support@atalanta-systems.com"]
  s.homepage    = "https://github.com/Atalanta/knife-cookbook-bump"
  s.summary     = %q{A Chef knife plugin designed to simplify a cookbook development workflow where cookbooks map onto git repositories.}
  s.description = s.summary

  s.rubyforge_project = "knife-cookbook-bump"

  s.files         = `git ls-files`.split("\n")
  s.test_files    = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.executables   = `git ls-files -- bin/*`.split("\n").map{ |f| File.basename(f) }
  s.require_paths = ["lib"]

  s.add_development_dependency "rspec"

  s.add_runtime_dependency "chef"
  s.add_runtime_dependency "grit"
end
