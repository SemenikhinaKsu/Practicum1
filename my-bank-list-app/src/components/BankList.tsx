import React from 'react';

interface Bank {
    id: number;
    name: string;
    location: string;
}

const banks: Bank[] = [
    { id: 1, name: 'Сбербанк', location: 'Москва' },
    { id: 2, name: 'ВТБ', location: 'Санкт-Петербург' },
    { id: 3, name: 'Альфа-Банк', location: 'Екатеринбург' },
    // Добавьте больше банков по вашему желанию
];

const BankList: React.FC = () => {
    return (
        <div className="container mt-5">
            <h1>Список банков</h1>
            <table className="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Название</th>
                        <th>Локация</th>
                    </tr>
                </thead>
                <tbody>
                    {banks.map(bank => (
                        <tr key={bank.id}>
                            <td>{bank.id}</td>
                            <td>{bank.name}</td>
                            <td>{bank.location}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default BankList;