<template>
  <div>
    <md-card-header>
      <div class="md-title">Case Study 3 - Interrupted</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          You finished the previous feature and picked up a new feature
          to <code>develop</code> (wow, aren’t you productive)!
          While you are working on your branch <code>feature/addPage</code>,
          your boss, Bob, asks you to fix an urgent production issue.
          The production code is running on <code>tag 1.0.1</code>.
        </p>
        <p>
          You told Bob that you will work on a fix immediately.
          However, since you have already started work on the new feature,
          you need to save your work first.
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
        >What git command should you use? Choose one of the following</p>
        <div class="mcq-option-container">
          <span>
             A. <code>git pull</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
             B. <code>git stash</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
             C. <code>git push feature/addPage</code>
          </span>
        </div>
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
