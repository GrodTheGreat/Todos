<template>
  <li class="md2-list-item">
    <div class="md2-list-item__container">
      <div class="md2-list-item__leading-content">
        <input type="checkbox" name="" id="" />
      </div>

      <div class="md2-list-item__main-content">
        <span class="md2-list-item__primary-text">Headline</span>
        <span class="md2-list-item__secondary-text">Supporting Text</span>
      </div>

      <div class="md2-list-item__trailing-content"></div>
    </div>
  </li>
</template>

<style lang="css" scoped>
li.md2-list-item {
  list-style: none;
  box-sizing: border-box;
  background-color: lightgray;
  height: 72px;
  width: 100%; /* This will need to be responsive */
}

.md2-list-item__container {
  display: flex;
  height: calc(100% - 16px);
  width: calc(100% - 8px);
  padding: 8px 16px;
}

.md2-list-item__leading-content {
  display: flex;
  justify-content: center;
  align-content: center;
}

.md2-list-item__main-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}
</style>
