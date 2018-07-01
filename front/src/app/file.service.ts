import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class FileService {
    private baseUrl: string = '/'

    constructor(private http: HttpClient) {}

    public upload(file: File) {
        return new Promise((resolve, reject) => {
            const formData: FormData = new FormData();
            formData.append('file', file, file.name);

            this.http.post(this.baseUrl + 'file', formData)
                .subscribe(resolve, reject);
        });
    }

    public query(key: string) {
        return new Promise((resolve, reject) => {
            const params = new HttpParams().set('key', key);

            this.http.get(this.baseUrl + 'file', {params})
                .subscribe(resolve, reject);
        });
    }
}
