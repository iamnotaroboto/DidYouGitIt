<template>
  <div>
    <md-card-header>
      <div class="md-title">Case Study 4 - Fix What is Broken</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          To work on the fix, you need to have your production code base ready.
          As you want to avoid working directly on <code>master</code> branch,
          you have to create a new branch <code>hotfix/productionFix</code>.
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
        > Which of the following commands create a new branch
                <code>hotfix/productionFix</code> from the release tag <code>1.0.1</code>?
                Choose one of the following</p>
        <div class="mcq-option-container">
          <span>
             A. <code>git checkout -b hotfix/productionFix 1.0.1</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
             B. <code>git branch hotfix/productionFix</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
              C. <code>git branch -d hotfix/productionFix 1.0.1</code>
          </span>
        </div>
      </div>
      <div class="indent-1">
              <p class="md-body-2">
                Now you have your branch ready, you can work on fixing the issue!
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
