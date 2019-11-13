<template>
  <div>
    <md-card-header>
      <div class="md-title">Introduction</div>
    </md-card-header>
    <md-card-content>
      <p>
        This course consists of 5 sections with mini-quizzes and 5 case study scenarios.
      </p>
      <p>
        This course covers Git commands that are commonly used
        in both work and school environments,
        and also advanced Git commands for learners with
        prior Git knowledge. By the end of the course,
        learners will be familiar with Git concepts,
        and able to use Git commands to work with
        Git repositories.
      </p>
      <p class="md-body-2">
        Pre-requisites:
      </p>
      <span>
        An understanding of version control:
        <a :href="'//www.youtube.com/watch?v=OqmSzXDrJBk'" target="_blank">
        https://www.youtube.com/watch?v=OqmSzXDrJBk </a>.
      </span>
      <br>
      <span>
        Git is installed on your machine. Tutorial:
        <a :href="'//git-scm.com/book/en/v2/Getting-Started-Installing-Git'" target="_blank">
        https://git-scm.com/book/en/v2/Getting-Started-Installing-Git </a>.
      </span>
      <p>
        The commands that you will learn in this course is by no means exhaustive,
        but you will gain a deeper understanding of Git with fundamental concepts.
        This course consists of 5 sections with 1 case study at the end.
        You will be given the opportunity at the end of the course to give back to the community
        by creating your own learning activity for git,
        so that other learners can benefit from your contribution.
      </p>
      <p>
        Now, let’s get started!
      </p>
      <md-card-actions>
        <md-button
          class="md-raised md-primary"
          v-on:click="onNext()">Start</md-button>
      </md-card-actions>
    </md-card-content>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'Intro',
  data: () => ({}),
  methods: {
    onNext() {
      this.$router.push('q1').catch((err) => {});
    },
  },
});
</script>
