<template>
  <div>
    <md-card-header>
      <div class="md-title">Case Study 1 - It's Monday</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          Now let’s practice with a case study!
          This case study offers various scenarios that might happen on a normal working day.

        </p>
        <p>
           Assume that you are working in a team on a software engineering project,
           and you report to Bob. It’s Monday! You have arrived in the office and begin work
           on your existing project.
        </p>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question 1</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p
          class="md-body-2"
        >What is the first step that you need to do? Choose one of the following</p>
        <div class="mcq-option-container">
          <span>
             A. <code>git pull master</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
             B. <code>git merge</code>
          </span>
        </div>
        <div class="mcq-option-container">
          <span>
              C. <code>git push</code>
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
            After running the above command,
            you realize that it cannot be completed
            because you have untracked modified files.
            If the changes are needed, What should you do? Choose one of the following</p>
          <div class="mcq-option-container">
            <span>
                A. <code>git commit -m “commit message”</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
                B. <code>git status</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span>
               C. <code>git add *, git commit -m “commit message”</code>
            </span>
          </div>
        </div>
     </md-card-content>
    <md-card-header>
        <div class="md-title">Question 3 </div>
    </md-card-header>
    <md-card-content>
        <div class="indent-1">
          <p class="md-body-2"
          >If the changes are to be discarded,
                   what should you do? Choose one of the following</p>
          <div class="mcq-option-container">
            <span>
                A. <code>git diff</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span >
               B. <code>git push</code>
            </span>
          </div>
          <div class="mcq-option-container">
            <span >
               C. <code>git revert</code>
            </span>
          </div>
        </div>
        <div class="indent-1">
                      <p>
                        Now, you are able to execute the first step again.
                      </p>
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
