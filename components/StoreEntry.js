import React from 'react';
import { StyleSheet, Text, View, Button, TextInput} from 'react-native';
import {postStore} from '../Api';

const StoreEntry = () => {

    const [storeName, updateStoreName] = React.useState('')
    const [storeLat, updateStoreLat] = React.useState('')
    const [storeLong, updateStoreLong] = React.useState('')
    const [storeCat, updateStoreCat] = React.useState('')
    
    return(
        <View>
        <TextInput
          placeholder = "What store?"
          onChangeText = {updateStoreName}
          value = {storeName}
        />
         <TextInput
          placeholder = "Latitude of Store"
          onChangeText = {updateStoreLat}
          value = {storeLat}
        />
        <TextInput
          placeholder = "Longitude of Store"
          onChangeText = {updateStoreLong}
          value = {storeLong}
        />
        <TextInput
          placeholder = "Store Category"
          onChangeText = {updateStoreCat}
          value = {storeCat}
        />
         <Button
          title="Submit Store"
          onPress={()=>{postStore(storeName, storeLat, storeLong, storeCat)}}
        />
        </View>
    );
}

export default StoreEntry;