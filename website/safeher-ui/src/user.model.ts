export enum ContactType {
    POLICE = "POLICE",
    POLICE_FROM_ANOTHER_CITY = "POLICE_FROM_ANOTHER_CITY",
    NEIGHBOR_FRIEND = "NEIGHBOR_FRIEND"
}

interface Contact {
    type: ContactType;
    first_name?: string;
    last_name?: string;
    phone?: string;
}

export enum DeviceType {
    LAMP = "LAMP",
    SMALL_DIFUUSER = "SMALL_DIFUUSER"
}

interface Address {
    street: string;
    number: number;
    floor: number;
    apartment: number;
}

interface Device{
    SSID: string;
    owner: string;
    type: DeviceType
}

export interface UserModel{
    first_name:string;
    last_name:string;
    age:number;
    address: Address;
    safeWord: string;
    contacts:Contact[];
    devices?: Device[];
}
