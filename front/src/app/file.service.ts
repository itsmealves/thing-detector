import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

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

            this.http.post(this.baseUrl + 'image', formData)
                .subscribe(resolve, reject);
        });
    }
}
