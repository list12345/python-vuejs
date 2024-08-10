<template>
  <div>
    <section>
      <h1>Edit Product</h1>
      <hr/><br/>

      <form @submit.prevent="updateProduct">
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
  name: 'EditProduct',
  data() {
    return {
        name: '',
        price: '',
        description: '',
        id: this.$route.params.id, //this is the id from the browser
    };
  },
  mounted: function() {
    this.GetProduct(this.id);
  },
  methods: {
    updateProduct() {
      var product_js = JSON.stringify({name: this.name, description: this.description, price: this.price});
      axios.put('/products/'+this.id, product_js,  {
          headers: {
              'Content-Type': 'application/json'
                  }
                  }).then(() => {
        this.$router.push('/products');
      });
    },
    GetProduct(productId) {
      axios.get('/products/' + productId).then((response) => {
        this.name = response.data.name;
        this.price = response.data.price;
        this.description = response.data.description;
      });
    },
  },
});
</script>
