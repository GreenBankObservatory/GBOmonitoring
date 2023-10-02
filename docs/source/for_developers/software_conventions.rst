***********************
Software Conventions
***********************


Git Standards
==============

Here we are looking to use the main / release conventions. 

We have one `main` branch that ebbs and flows with the code. And time locked release branches that will hold the code published to the production webpage. This can also include development branches.  

Here is the branches:

`main` - This branch will hold the latest and greatest code, you can push here to share your code, but it will not impact the production website. 

`release_#.#` - this is released on a rolling basis and the production webpage will look at the most recent release, ex. `release_1.0` - here when the branch is created and released, the main branch can continue receiveing developments and working towards the next release, which will be the increased release number, ex. `release_2.0`

`<>_dev` - these are our development branches. Currently we have `cat_dev` and `kasey_dev`. These can be specific to the developer or to the improvement, but they should have describtive names and all end with the `_dev` convention.

See below for a git graph demonstrating the convention defined git indexing. 

.. mermaid::

    gitGraph
        commit
        commit
        branch kasey_dev
        checkout kasey_dev
        commit
        commit
        checkout main
        merge kasey_dev
        commit
        commit
        branch release_1.0
        checkout release_1.0
        commit
        checkout main
        commit
        checkout kasey_dev
        commit
        checkout main
        merge kasey_dev
        commit
        branch release_2.0
        commit
        checkout main
        commit
        checkout kasey_dev
        commit
        checkout main
        commit


Webpage Standards
=================

We have several options for the webpage releases. 

monitoring.gb.nrao.edu - This is our produciton page. Here we will alwasy be pointing at the newest release branch

monitoring-beta.gb.nrao.edu - This is our beta page. Here we will be looking also at the most recent release branch, but this can be changed to the main branch fro testing as well if needed

development hosted pages - These are developer hosted sites used for testing. These will be used to test releases and main branch. But will be promarily used to test the development branches `_dev`. These pages will be taken up and down from teh command prompts so they will likely not be left on overnights.