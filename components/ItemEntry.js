import React from 'react';
import { StyleSheet, Text, View, Button, TextInput} from 'react-native';
import {postItem} from '../Api';

const ItemEntry = () => {

    const [itemName, updateName] = React.useState('')
    const [category, updateCategory] = React.useState('')
    const [amount, updateAmount] = React.useState('')
    const [storeId, updateStore] = React.useState('')
    
    return(
        <View>
        <TextInput
          placeholder = "What did you find?"
          onChangeText = {updateName}
          value = {itemName}
        />
         <TextInput
          placeholder = "Category of Item"
          onChangeText = {updateCategory}
          value = {category}
        />
        <TextInput
          placeholder = "Amount of Item"
          onChangeText = {updateAmount}
          value = {amount}
        />
        <TextInput
          placeholder = "Store Id"
          onChangeText = {updateStore}
          value = {storeId}
        />
        <Button
          title="Submit Item"
          onPress={()=>{postItem(itemName, category, amount, storeId)}}
        />
        </View>
    );
}

export default ItemEntry;