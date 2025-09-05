
<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom border-danger border-3">
      <div class="container-fluid">
        <a class="navbar-brand p-0" href="#/">
          <img src="/favicon.ico" alt="로고" style="width:32px; height:32px;" />
        </a>
        <div class="flex-grow-1"></div>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 flex-row gap-3">
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/movies">영화조회</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/review-search">리뷰검색</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" to="/recommend">영화추천</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <main class="container mt-4">
    <RouterView/>
  </main>
</template>

<script setup>
</script>

<style scoped>
main {
  min-height: 80vh;
}
.navbar {
  border-top: 3px solid #dc3545 !important;
}
</style>
