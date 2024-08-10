<template>
  <div>
    <section>
      <h1>Add new Product</h1>
      <hr/><br/>

      <form @submit.prevent="addProduct">
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" name="name" v-model="name" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Description:</label>
          <textarea
            name="description"
            v-model="description"
            class="form-control"
          ></textarea>
        </div>
        <div class="mb-3">
          <label for="price" class="form-label">Price:</label>
          <input type="text" name="price" v-model="price" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      name: '',
      price: '',
      description: '',
    };
  },
 methods: {
    addProduct() {
      console.log(this.name);
      var product_js = JSON.stringify({name: this.name, description: this.description, price: this.price});
      axios.post('/products', product_js,  {
          headers: {
              'Content-Type': 'application/json'
                  }
                  }).then(() => {
        // Optionally, navigate to the list view
        this.$router.push('/products');
      });
    },
  },
});
</script>


