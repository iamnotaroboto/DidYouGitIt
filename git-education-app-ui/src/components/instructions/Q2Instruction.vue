<template>
  <div>
    <md-card-header>
      <div class="md-title">Section 2 - Working Directory and Staging Area</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p>
          From the previous question,
          you would have understood the difference between remote and local repositories.
          Now we will introduce the working directory.
        </p>
        <p>
          A <span class="md-body-2">working directory / tree</span> is the area where you are
          currently working or where your files live.
          It is also known as the “untracked” area of git.
          Any changes to files will be marked and seen in the working directory.
          If you make any changes and do not explicitly save them via git,
          you will lose the changes made.
        </p>
        <p>
          To see the changes in your working directory,
          use <code>git status</code>. If there is nothing,
          you will see <code>nothing to commit, working directory clean</code>.
        </p>
        <p>
          Let’s create a file named test.py in the repository from the previous section.
          Running <code>git status</code> again, you will see the following:
          <code>Untracked files: test.py</code>
        </p>
        <p>
          At this point in time, git knows nothing about the untracked files.
          The <span class="md-body-2">staging area</span>
          is where git tracks and saves changes that occur in files.
          These saved changes reflect in the .git directory.
          To move test.py from working directory to the staging area,
          or <span class="md-body-2">staging</span>, so that git recognizes it,
          use the command: <code>git add [file]</code>.
          Example: <code>git add test.py</code>
        </p>
        <p>
          To discard all changes made to test.py,
          we can use <code>git revert [file]</code>.
          <br>Example: <code>git revert test.py</code>
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
            A revert operation will take the specified commit,
            inverse the changes from that commit, and create a new "revert commit"
          </span>
        </div>
        <div class="mcq-option-container">
          <span>B.</span>
          <span class="indent-1">
            The Git directory is where Git stores the metadata and object database for your project
          </span>
        </div>
        <div class="mcq-option-container">
          <span>C.</span>
          <span class="indent-1">When you run git status,
            you can only see staged files (currently in your index)</span>
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
