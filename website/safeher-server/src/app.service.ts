import { HttpService, Injectable } from '@nestjs/common';
import { Observable, of } from 'rxjs';

const SERVER = 'http://localhost:9000/fake';

@Injectable()
export class AppService {

  constructor(private readonly httpService: HttpService) {

  }

  registerUser(user: any): Observable<any> {
    // return this.httpService.post(SERVER)
    console.log(user);
    return of({});
  }
}
