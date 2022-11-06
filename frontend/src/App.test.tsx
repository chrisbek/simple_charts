import React from 'react';
import {render, screen} from '@testing-library/react';
import App from './App';

global.ResizeObserver = require('resize-observer-polyfill')

test('renders learn react link', () => {
    render(<App/>);
    const linkElement = screen.getByText(/Share/i);
    expect(linkElement).toBeInTheDocument();
});
