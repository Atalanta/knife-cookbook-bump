Knife (Cookbook) Bump
=====================

Knife bump is a knife plugin designed to simplify a cookbook development workflow where cookbooks map onto git repositories.

Rationale
=========

For any infrastructure developer who works with more than one Opscode Hosted Chef Organization, or has more than one Chef Server (perhaps mapping to a different project, client, or job), the mainstream cookbook development pattern of using the Ospcode Community site, perhaps augmented by your own or third party cookbooks in your Chef repository, doesn't scale very well.  Cookbooks are code - it makes sense to encourage code resuse wherever possible, and bug fixes and enhancements to cookbooks used on one project/organization ought to benefit other organizations.  This proves to be trickier than it sounds, when eeping a collection of dozens of these cookbooks.  These cookbooks are likely to be used in lots of different combinations for different projects/organizations,  requiring a great deal of flexibility.

Managing versioning of this code with a single project is made easy because of the versioning and constraining system that Chef server allows.  We can upload every new version to the Chef server, and constrain which versions are used by employing Chef Environments.  When working with multiple organizations or project, trying to use the Chef server as the authoritative source of versioned cookbooks would require all orgs to have all cookbooks - and every time a change was made, the cookbook(s) being pushed to all orgs/servers.  No, the canonical source of versioning needs to be the version control system in which the cookbook resides.  The normal pattern for cookbooks is to keep them within a Chef repository.  However, Git makes it difficult to tag and branch based on subdirectories.  If I have a single repository, and I make a change to the mongodb cookbook, and increment its version in the metadata, and tag that commit, I will be able to pull the commit again in the future.  Unfortunately, even with the advent of sparse checkouts, I can't really checkout just that directory for just that repository.  The situation becomes much more complicated when we try to scale this over a large number of cookbooks.  Suppose for client A I want mongodb-1.0.1, nginx-1.1.2 and mysql-1.2.6, I can't guarantee that I can find a place in the commit history where all three cookbooks were at the correct version.  I'd need to clone the repo (perhaps sparsely) three times.  Rarely does a project use as few as three cookbooks, so it's apparent that this isn't an elegant solution.  It turns out that, on considersation, the best way to guarantee the degree of flexibility required to work with multiple clients and multiple cookbooks and versions, the best model is to have one git repo per cookbook.

Workflow
========

The idea of having dozens of cookbook repositories sounds initially clumsy and inelegant, but it's actually a very effective strategy.  We want the following

* A centralised, versioned history of all fixes and improvements for a given cookbook
* To reinforce the idea of modularity - cookbooks should solve problems in one domain, and should ship the documentation and support code to achieve this in one place
* To improve the shareability of cookbooks, both between projects and organizations, and within the broader Chef community.  Mapping cookbooks onto Git repositories opens up the same collaborative benefits of Github and similar tools to all infrastructure developers

In order to make the idea workable, it's important to develop a reliable and repeatable workflow which describes the lifecycle of cookbook development.  The following has been tested by Atalanta Systems across a number of clients and technology platforms, and represents a proven approach upon which to base such a workflow:

* Create a git repository for every cookbook you're going to develop on or contribute to.
* If you're using one of the cookbooks already residing in a dedicated repository, simply fork it as any other software project
* If you wish to use the Opscode community cookbooks as a starting point, either download the cookbook from the community site using knife, or a browser, or pull the code from the opscode/cookbooks Github repository.  Be aware the Opscode cookbooks repo is fast-moving and in the spirit of Debian Sid could well be in an unstable state - if it breaks, you get to keep the pieces.
* As you add features or fix bugs, when you're satisfied with your code, increment the version in the cookbook metadata and README and tag the repository with the same name, then push your changes and your tags to Github or your Git server.
* Curating disparate cookbooks into a meaningful whole can be done manually, but a powerful approach is to use `librarian-chef`, which introduces the concept of a Cheffile, modelled after Ruby's bundler.  A Cheffile simply describes the cookbooks needed for the organization/project, the location of the source code, and any version constraints.  `librarian-chef` also attempts to solve dependencies based on cookbook metadata.  See https://github.com/applicationsonline/librarian for more information.
* Testing cookbooks and guaranteeing stability for production can be achieved using Chef Environments.  Create an environment called `stable`, and use cookbook version constraints and freezing to provide certainty around the use of known-good and tested cookbooks.  Create one or more `unstable` environments to explore and develop cookbooks and their dependencies.  Bootstrap nodes into stable or unstable environments depending on whether you want to experiment and develop, or provide a repeatable and guaranteed set of cookbooks.

Usage
=====

Knife bump is designed to automate as much of the workflow described above.  At present, the following functionality is supported:

* Bumping of cookbook metadata
* Tagging of cookbook git repositories

Knife bump is not yet packaged as a Rubygem, so for now, you can just drop the main code, lib/cookbook-bump/bump.rb in your plugins/knife directory, and knife will find it.  It has a dependency on the `grit` gem to provide object-oriented access to Git repositories.

Bumping
-------

Cookbooks follow a simple three level versioning pattern.  Knife bump allows the patch, minor or major version to be bumped, and will automatically update the version in the metadata.

$ knife cookbook create netscape
** Creating cookbook netscape
** Creating README for cookbook: netscape
** Creating metadata for cookbook: netscape
$ knife bump netscape patch
Bumping patch level of the netscape cookbook from 0.0.1 to 0.0.2
$ grep version cookbooks/netscape/metadata.rb 
version          "0.0.2"
$ knife bump netscape minor
Bumping minor level of the netscape cookbook from 0.0.2 to 0.1.2
$ grep version cookbooks/netscape/metadata.rb 
version          "0.1.2"

Tagging
-------

*In development*

Supplying the --tag option will additionally tag the git repository corresponding to the cookbook you're working on.  Knife bump attempts to find this repository intelligently, but will ask for confirmation before tagging.  It will also warn you if it thinks the name of the repository it found doesn't sound like a plausible name for the cookbook.


Tests
-----

The core functionality is tested using rspec.  The plugin mechanics are assumed to have been tested by Opscode.

Changes/Roadmap
---------------

No formal release yet.

