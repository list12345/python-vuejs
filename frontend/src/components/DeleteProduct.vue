<template>
  <div>
    <h2>Delete Product</h2>
    <p>Are you sure you want to delete this Product?</p>
    <button @click="confirmDelete">Yes</button>
    <button @click="cancelDelete">No</button>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DeleteProduct',
  methods: {
    confirmDelete() {
       axios.delete('/products/' + this.$route.params.id).then((response) => {
        console.log(response);
        this.$router.push('/products');
      });
    },
    cancelDelete() {
      // Navigate back to the list view or close the modal
      this.$router.push('/products');
    },
  },
});
</script>
