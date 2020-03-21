import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { SearchBar } from 'react-native-elements';

export default class App extends React.Component {
  state = {
    search: '',
  }
  updateSearch = search => {
    this.setState({search});
  };
  render(){
    const {search} = this.state;
    return (
      <View style={styles.container}>
        <Text>What do you need?</Text>
        <Text>{search}</Text>
        <SearchBar 
          placeholder="Type Here..."
          onChangeText = {this.updateSearch}
          value = {search}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
