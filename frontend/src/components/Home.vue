<template lang="html">
    <div class=" w-full bg-backgroundColor">
        <main class="min-h-screen">
            <!-- Header -->
            <div id="header" class="w-full">
                <div class="pt-5 flex flex-col justify-center rounded-xl">
                   <img id="headImg" src="https://64.media.tumblr.com/36967d731108d643d9b74bb3c5d2b5e1/747e52494a39b5da-e4/s1280x1920/b9b00fbfeb83f513fe3d09634c9dda906d7b3198.gifv"/>
    
                </div>
                <div class="pt-12 justify-center">
                    <label class="text-xl font-semibold">
                    
                    </label>
                </div>
            </div>
            <!-- Body -->
            <div id="body" class="mt-5 mx-5 mb-5 lg:flex lg:flex-row md:flex md:flex-col">
                <div class="lg:w-112 md:w-full">
                    <form
                      @submit.prevent="estimateCarPrice"
                      class="px-8 py-5 space-y-2 rounded-xl bg-containers"
                    >
                      <!-- Brand field -->
                      <div>
                        <label class="text-xl font-bold text-text block"> Marca </label>
                        <input
                          type="text"
                          name="brand"
                          v-model="brand"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Password field -->
                      <div class="">
                        <label class="text-xl font-bold text-text block"> Modelo </label>
                        <input
                          type="text"
                          name="model"
                          v-model="model"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Year field -->
                      <div class="">
                        <label class="text-xl font-bold text-text block"> Año </label>
                        <input
                          type="number"
                          name="brand"
                          v-model="year"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Kilometers field -->
                      <div class="">
                        <label class="text-xl font-bold text-text block"> Kilometraje </label>
                        <input
                          type="number"
                          name="kilometers"
                          v-model="kilometers"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Motor field -->
                      <div class="">
                        <label class="text-xl font-bold text-text block"> Motor </label>
                        <input
                          type="text"
                          name="motor"
                          v-model="motor"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500"
                        />
                      </div>
                      <!-- Transmission field -->
                      <div class="">
                        <label class="text-xl font-bold text-text block"> Transmisión </label>
                        <select
                          name="transmission"
                          v-model="transmission"
                          class="block w-full p-1 rounded border-2 border-solid border-gray-500">
                            <option value="Automatica">Automática</option>
                            <option value="Mecanica">Mecánica</option>
                            <option value="Automatica secuencial">Automática secuencial</option>
                        </select>
                      </div>
                      <!-- Submit button -->
                      <div class="pt-3 flex justify-center">
                        <button
                          class="py-2 px-4 bg-buttonF hover:bg-buttonB  text-text flex justify-center font-semibold text-m"
                        >
                          PREDECIR PRECIO
                        </button>
                      </div>
                    </form>
                    <div class="lg:w-112 border bg-containers rounded-xl mt-5 px-8 py-5 font-semibold md:w-full text-lg">
                      <label class="text-xl font-semibold text-text">
                      El precio estimado para su carro es
                      </label>
                       &nbsp; <label class="text-price text-xl"> {{ price }} </label>
                    </div>
                </div>        
                <!-- rotating car gif -->
                <div class="w-full flex flex-col justify-center lg:ml-10">
                    <img @click="changeCarImg" id="carImg" src="https://drive.google.com/uc?export=view&id=1y0PZkQ5PNdlax_51j-VbvW_re7a11cb_" />
                </div>
            </div>
            <!-- Footer -->
            <div id="footer" class="w-full bg-gray-100 h-16 mt-16">
                <div class="p-5 text-text"> © 2021 ICESI University </div>
            </div>
        </main>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Main",
  data() {
    return {
      brand: "",
      model: "",
      year: "",
      kilometers: "",
      motor: "",
      transmission: "",
      price: "",
      img_count: 0,
      cars_imgs: [
        "https://drive.google.com/uc?export=view&id=1Qaoqn1xozn2kNRSFYsKiSNtdezcN-L_-",
        "https://drive.google.com/uc?export=view&id=1y0PZkQ5PNdlax_51j-VbvW_re7a11cb_",
        "https://drive.google.com/uc?export=view&id=15QEtVDUfzi-APJzbY6hCPG3SHZn4ZUSa",
        "https://drive.google.com/uc?export=view&id=1TA8lquwfZCObw6woYEFfEygd77u4z4-W",
        "https://drive.google.com/uc?export=view&id=1jeUZzbC1W8ZKJGGUjSbdVcqTt3r0GLTT",
        "https://drive.google.com/uc?export=view&id=1sQAC2_PGJlG3cha_LV1k1rB9l5leqBQK",
        "https://drive.google.com/uc?export=view&id=16ix8mPDheXOnFm3G0DAFSBks8rLal5m1",
      ],
    };
  },
  methods: {
    changeCarImg() {
      if (this.img_count == 6) {
        this.img_count = 0;
        document.getElementById("carImg").src = this.cars_imgs[this.img_count];
      } else {
        this.img_count += 1;
        document.getElementById("carImg").src = this.cars_imgs[this.img_count];
      }
    },
    estimateCarPrice() {
      const path = "http://localhost:5000/api/v1.0/estimateCarPrice";
      axios
        .post(path, {
          brand: this.brand,
          model: this.model,
          year: this.year,
          kilometers: this.kilometers,
          motor: this.motor,
          transmission: this.transmission,
        })
        .then((response) => {
          this.price = "$ " + response.data;
        })
        .catch((error) => {
          console.error(error);
        });

      // clear fields
      this.brand = "";
      this.model = "";
      this.year = "";
      this.kilometers = "";
      this.motor = "";
      this.transmission = "";

      this.changeCarImg();
    },
  },
  created() {},
};
</script>