<template>
  <div>
    <md-card-header>
      <div class="md-title">Section 3 - Synchronizing Staging Area and Local Repository</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          The local repository is everything in your .git directory.
          It is the area that saves everything including your checkpoints or commits.
          You may also think of the local repository as a versioned history.
        </p>
        <p>
          At this point we can choose to unstage our file (test.py)
          by using the command
          <code>git reset test.py</code>,
          make further changes that we can stage,
          save our changes using
          <code>git stash</code> and
          recover them when needed using
          <code>git stash apply</code>,
          or commit our changes to the local repository.
        </p>
        <p>
          Let’s commit our changes to the local repository.
          A commit is simply a checkpoint instructing Git to track all changes
          that have occurred up to this point using our last commit as a comparison.
          We can commit with the command
          <code>git commit -m “commit message”</code>.
        </p>
        <p>
          We could have done both the
          <span class="md-body-2">add and commit</span>
          in the same command by running the
          following command while having modified files that were not yet in
          staging:
          <code>git commit -am “commit message here”</code>.
        </p>
        <p>Note: A good commit message conveys a summary of changes</p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p class="md-body-2">Which of the following is incorrect?</p>
        <div class="mcq-option-container">
          <span>A.</span>
          <span class="indent-1">
            The
            <code>git add</code>
            command adds a change in the working directory to the staging area
          </span>
        </div>
        <div class="mcq-option-container">
          <span>B.</span>
          <span class="indent-1">
            When using
            <code>git reset --hard HEAD~1</code> you will
            remove the last commit from the current branch,
            but the file changes will stay in your working tree
          </span>
        </div>
        <div class="mcq-option-container">
          <span>C.</span>
          <span class="indent-1">
            Staged means that you have marked a
            modified file in its current version to go
            into your next commit snapshot
          </span>
        </div>
        <div class="mcq-option-container">
          <span>D.</span>
          <span class="indent-1">
            Modified means that you have changed
            the file but have yet to commit it
            to your local repository.
          </span>
        </div>
      </div>
    </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Q3Instruction',
  data: () => ({}),
});
</script>
