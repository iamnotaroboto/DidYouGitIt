<template>
  <div>
    <md-card-header>
      <div class="md-title">Case Study 5 - Retrieve Previous Work</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          After working intensely, you fixed the issue,
          pushed the code fix to your hotfix branch and also merged to master.
        </p>
        <p>
          You plan to continue working on your <code>feature/addPage</code> branch(from before).
        </p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p class="md-body-2">
         How do you retrieve your unfinished work
              before Bob called you to work on the production issue?
              Choose one of the following</p>
        <div class="mcq-option-container">
          <span>
             A. <code>git pull, git stash pop</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
             B. <code>git checkout feature/addPage, git stash apply</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
              C. <code>git commit -m "add page", git push</code>
            </span>
        </div>
      </div>
      <div class="indent-1">
              <p>
                Finally you finished your work for the day!
                Remember to commit, push all your changes
                and merge to master before you leave the office.
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
