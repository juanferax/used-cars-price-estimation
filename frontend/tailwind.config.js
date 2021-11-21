module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors:{
        backgroundColor: '#1E1C40',
        buttonF: '#AC47AA',
        buttonB: '#AD71AC',
        containers: '#3C396D',
        
    },
    textColor:{
      text: '#F1F1F1',
      price: '#AC47AA',
    },
    extend: {
      spacing: {
        "102": "28rem",
        "112": "36rem"
      }
    }
  },
  variants: {
    extend: {}
  },
  plugins: []
};
