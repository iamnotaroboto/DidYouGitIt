<template>
  <div>
    <md-card-header>
      <div class="md-title">Section 1 - Creating A Repository</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p class="md-body-2">1. Creating a repository from scratch</p>
        <div class="indent-1">
          To create a Git repository locally from scratch,
          you can initialize a local git repository with the following command:
          <div><code>git init [name of repository]</code></div>Example:
          <div><code>git init my-first-git-repository</code></div>
        </div>
        <br />
        <p class="md-body-2">2. Downloading from an existing repository</p>
        <div class="indent-1">
          To do so, we clone the remote repository with the following command:
          <div><code>git clone [url]</code></div>Example:
          <div><code>git clone https://github.com/keras-team/keras.git</code></div>
        </div>
      </div>
    </md-card-content>
    <md-card-header>
      <div class="md-title">Question</div>
    </md-card-header>
    <md-card-content>
      <div class="indent-1">
        <p
          class="md-body-2"
        >Which of the following about local and remote repositories is incorrect?</p>
        <div class="mcq-option-container">
          <span>A.</span>
          <span class='indent-1'>
            Local repositories reside on the computers of team members.
            In contrast, remote repositories are hosted on a server
            that is accessible for all team members
          </span>
        </div>
        <div class="mcq-option-container">
          <span>B.</span>
          <span class='indent-1'>
            Remote repositories are thought as a means for sharing
            and exchanging code between developers,
            not for actually working on files
          </span>
        </div>
        <div class="mcq-option-container">
          <span>C.</span>
          <span class='indent-1'>
            You don’t need network connection to work on Remote repository
          </span>
        </div>
      </div>
    </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Q1Instruction',
  data: () => ({}),
});
</script>
