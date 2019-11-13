<template>
  <div>
    <md-card-header>
      <div class="md-title">Case Study 2 - It's time to publish your changes</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          You have developed and tested a feature on your local branch.
          As you work, you added and committed the changes to your local repository.
          Now you want to include this feature in the official working version
          of your remote repository (<code>master</code> branch).
        </p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question 1</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p class="md-body-2">
         First, to sync the changes to the remote branch: <code>feature/addButton</code>.
         What should you do
         assuming no one else is working on the same branch as you?
         Choose one of the following</p>
        <div class="mcq-option-container">
          <span>
              A. <code>git diff feature/addButton master</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
              B. <code>git stash</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
              C. <code>git push feature/addButton</code>
            </span>
        </div>
      </div>
    </md-card-content>
    <md-card-header>
        <div class="md-title">Question 2</div>
    </md-card-header>
    <md-card-content>
        <div class="indent-1">
          <p class="md-body-2">
            To ensure that there is no merge conflict when you eventually
            merge into the master branch,
            you ran git pull to retrieve the changes from the master branch into your local branch.
         </p>
         <p class="md-body-2">
            Before you merge the feature branch <code>feature/addButton</code>
            to <code>master</code>,
            you remember that you need to ensure that all your changes are included.
            Which command can you use to do that? Choose one of the following</p>
          <div class="mcq-option-container">
            <span>
                A. <code>git diff feature/addButton master</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
               B. <code>git stash</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
               C. <code>git push feature/addButton</code>
            </span>
          </div>
        </div>
     </md-card-content>
    <md-card-header>
        <div class="md-title">Question 3</div>
    </md-card-header>
    <md-card-content>
        <div class="indent-1">
          <p class="md-body-2"
          >  You have verified that your feature branch is ready to merge.
          Which command should you run? Choose one of the following</p>
          <div class="mcq-option-container">
            <span>
                A. <code>git checkout master, git merge feature/addButton</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
                B. <code>git branch -d master</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
                C. <code>git reset --hard HEAD</code>
            </span>
          </div>
        </div>
        <div class="indent-1">
           <p class="md-body-2">
              Enter your solution for the three questions(e.g. ABC, BBB, CAB, or ...)
              in the input block and click on the SUBMIT button
           </p>
        </div>
     </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Q2Instruction',
  data: () => ({}),
});
</script>
