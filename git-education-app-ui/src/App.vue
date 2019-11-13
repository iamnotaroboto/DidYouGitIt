<template>
  <div>
    <md-app md-waterfall md-mode="fixed">
      <md-app-toolbar class="md-large md-dense md-primary">
        <div class="md-toolbar-row">
          <div class="md-toolbar-section-start">
            <span class="md-title">Did you Git it?</span>
          </div>
        </div>
        <div class="md-toolbar-row">
          <md-tabs md-sync-route class="md-primary">
            <md-tab id="tab-intro" md-label="Introduction" to="/intro" exact></md-tab>
            <md-tab id="tab-q1" md-label="Q1" to="/q1" exact></md-tab>
            <md-tab id="tab-q2" md-label="Q2" to="/q2" exact></md-tab>
            <md-tab id="tab-q3" md-label="Q3" to="/q3" exact></md-tab>
            <md-tab id="tab-q4" md-label="Q4" to="/q4" exact></md-tab>
            <md-tab id="tab-q5" md-label="Q5" to="/q5" exact></md-tab>
            <md-tab id="tab-c1" md-label="C1" to="/c1" exact></md-tab>
            <md-tab id="tab-c2" md-label="C2" to="/c2" exact></md-tab>
            <md-tab id="tab-c3" md-label="C3" to="/c3" exact></md-tab>
            <md-tab id="tab-c4" md-label="C4" to="/c4" exact></md-tab>
            <md-tab id="tab-c5" md-label="C5" to="/c5" exact></md-tab>
          </md-tabs>
        </div>
      </md-app-toolbar>
    </md-app>
    <router-view />
  </div>
</template>
<script lang='ts'>
import Vue from 'vue';

export default Vue.extend({
  name: 'App',
  mounted() {
    this.$router.replace('intro').catch((err) => {});
  },
});
</script>
<style lang="scss">
.md-app {
  background-color: var(--md-theme-default-primary, #448aff)!important;
}
code {
  background-color: #eeeeee;
  padding: 3px;
}
.md-button:disabled {
  color: var(
    --md-theme-default-disabled-on-background,
    rgba(0, 0, 0, 0.26)
  ) !important;
}
.indent-1 {
  padding-left: 15px;
  padding-right: 15px;
}
.mcq-option-container {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}
.md-tabs-navigation .md-button-content {
  padding: 3px;
}
</style>
