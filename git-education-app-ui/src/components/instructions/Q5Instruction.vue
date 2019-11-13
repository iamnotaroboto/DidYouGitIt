<template>
  <div>
    <md-card-header>
      <div class="md-title">Section 5 - Branching and Merging</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          Each repository can have one or more branches. The main branch
          — the one where all changes eventually get merged back into,
          and is called the master.
          We suggest not to work on the master branch directly as
          it is the official working version of your project.
          Instead you should create your own branches for your work on
          features and fixes and eventually merging back to master.
          There are many discussions on when to branch and whether to branch
          which we will not cover them in this course.
        </p>
        <p>
          To
          <span class="md-body-2">see all the branches</span>
          in the project, even those not in the local repository,
          use command
          <code>git branch -a</code>.
        </p>
        <p>
          To
          <span class="md-body-2">create a new branch</span>, use
          <code>git checkout -b [newBranchName]</code>
          Example:
          <code>git checkout -b myNewBranch</code>.
          The -b command tells git to create the new branch and switch to it.
          Git is always watching what you do and keeps a special pointer
          alled HEAD which indicates the local branch you are currently on.
          You may use
          <code>git status</code> to view the branch you are on.
        </p>
        <p>
          When you are done working on your branch,
          you would want to
          <span class="md-body-2">merge</span> the changes to the master branch.
          The best practice is to first merge any changes from master into your branch.
          To do so, we will use
          <code>git merge master</code>.
        </p>
        <p>
          Occasionally, the merge doesn’t go smoothly. For example,
          if you changed the same part of the same file differently in the
          two branches you are merging,
          Git won’t be able to merge them cleanly and Git will tell
          you that there is a
          <span class="md-body-2">merge conflict</span>.
          Anything that has merge conflicts and hasn’t been resolved is listed as unmerged.
        </p>
        <p>
          Git adds standard conflict-resolution markers to the files that have conflicts,
          so you can open them manually and resolve those conflicts.
          If you want to use a graphical tool to resolve these issues,
          you can run
          <code>git mergetool</code>. Once the conflict is resolved, commit and push.
        </p>
        <p>
          Finally to merge the changes to the master branch,
          we need to be on the master branch. Use this command
          <code>git checkout master</code>
          for switching to an existing branch. Once on the master branch,
          we will use
          <code>git merge myNewBranch</code>.
        </p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p class="md-body-2">Which command below renames the branch name to &lt;branch>?</p>
        <div class="mcq-option-container">
          <span>A.</span>
          <span class="indent-1">git remote rm &lt;name></span>
        </div>
        <div class="mcq-option-container">
          <span>B.</span>
          <span class="indent-1">git branch -m &lt;branch></span>
        </div>
        <div class="mcq-option-container">
          <span>C.</span>
          <span class="indent-1">git branch -D &lt;BRANCH></span>
        </div>
        <div class="mcq-option-container">
          <span>D.</span>
          <span class="indent-1">git rebase &lt;base></span>
        </div>
      </div>
    </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Q5Instruction',
  data: () => ({}),
});
</script>
