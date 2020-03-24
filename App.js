import React from 'react';
import { StyleSheet, Text, View, Button, TextInput} from 'react-native';
import { SearchBar } from 'react-native-elements';


import ItemEntry from './components/ItemEntry'
import StoreEntry from './components/StoreEntry'

const App = ()=>{
  




    return (
      <View style={styles.container}>
        <Text>Item</Text>
        <ItemEntry/>
        <Text>Store</Text>
        <StoreEntry />

       

      </View>
    );
  }




const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;