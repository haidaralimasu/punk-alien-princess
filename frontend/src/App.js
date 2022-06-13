import React from "react";
import GlobalStyle from "./styles/globalStyles";
import { Navbar, Footer, InfoSection } from "./components";

const App = () => {
  return (
    <div>
      <GlobalStyle />
      <Navbar />
      <InfoSection />
      <Footer />
    </div>
  );
};

export default App;
