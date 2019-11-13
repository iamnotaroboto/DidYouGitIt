<template>
  <div>
    <md-card-header>
      <div class="md-title">Section 4 - Synchronizing Local Repository and Remote Repository</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          So far all of our changes, including our repository changes have been local.
          Now it’s time to sync up our local and remote repositories
          (do make sure you have valid remote repository credentials).
          There are several scenarios that can occur:
        </p>
        <p class="md-body-2">
          1. Out-of-date local repository which happens if others
          update the remote repository with changes.
        </p>
        <p class="indent-1">
          In this scenario, the <code>git fetch</code> command grabs all the latest commits
          from the remote repository (origin).
          Note that it does not add them into your local repository.
        </p>
        <p class="indent-1">
          To have the changes applied to your local repository,
          use the command <code>git pull</code>,
          which which performs a git fetch followed by a git merge
          (we will cover this and possible merge conflicts in the next section) under the covers.
        </p>
        <p class="md-body-2">
          2. Up-to-date local repository
        </p>
        <p class="indent-1">
          Now that your repository is up-to-date,
          you want to transfer the changes from your local repository to the remote repository.
          You can do this with the command <code>git push</code>.
        </p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p
          class="md-body-2"
        >Which of the following is incorrect?</p>
        <div class="mcq-option-container">
          <span>A.</span>
          <span class="indent-1">
            The git fetch command downloads commits, files,
            and refs from a remote repository into your local repository
          </span>
        </div>
        <div class="mcq-option-container">
          <span>B.</span>
          <span class="indent-1">
            If any of the remote changes overlap with local uncommitted changes,
            the merge will be automatically canceled and the working tree untouched
          </span>
        </div>
        <div class="mcq-option-container">
          <span>C.</span>
          <span class="indent-1">
            Pushing doesn’t have the potential to overwrite changes
          </span>
        </div>
      </div>
    </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Q4Instruction',
  data: () => ({}),
});
</script>
